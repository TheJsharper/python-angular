const http = require('http');
const net = require('net');

const TARGET_HOST = 'localhost';
const TARGET_PORT = 4200;
const PROXY_PORT = 4300;

function addIsolationHeaders(headers) {
  return {
    ...headers,
    'cross-origin-opener-policy': 'same-origin',
    'cross-origin-embedder-policy': 'require-corp',
  };
}

const server = http.createServer((req, res) => {
  const options = {
    host: TARGET_HOST,
    port: TARGET_PORT,
    method: req.method,
    path: req.url,
    headers: {
      ...req.headers,
      host: `${TARGET_HOST}:${TARGET_PORT}`,
    },
  };

  const proxyReq = http.request(options, (proxyRes) => {
    res.writeHead(proxyRes.statusCode || 500, addIsolationHeaders(proxyRes.headers));
    proxyRes.pipe(res);
  });

  proxyReq.on('error', (err) => {
    res.writeHead(502, { 'content-type': 'text/plain' });
    res.end(`Proxy error: ${err.message}`);
  });

  req.pipe(proxyReq);
});

// Forward websocket upgrades (for dev HMR and tooling sockets).
server.on('upgrade', (req, clientSocket, head) => {
  const upstreamSocket = net.connect(TARGET_PORT, TARGET_HOST, () => {
    const requestLine = `${req.method} ${req.url} HTTP/${req.httpVersion}\r\n`;
    const headerLines = Object.entries({
      ...req.headers,
      host: `${TARGET_HOST}:${TARGET_PORT}`,
    })
      .map(([k, v]) => `${k}: ${v}`)
      .join('\r\n');

    upstreamSocket.write(`${requestLine}${headerLines}\r\n\r\n`);
    if (head && head.length) upstreamSocket.write(head);

    clientSocket.pipe(upstreamSocket).pipe(clientSocket);
  });

  upstreamSocket.on('error', () => {
    clientSocket.destroy();
  });

  clientSocket.on('error', () => {
    upstreamSocket.destroy();
  });
});

server.listen(PROXY_PORT, () => {
  // eslint-disable-next-line no-console
  console.log(`Isolated dev proxy running: http://localhost:${PROXY_PORT} -> http://localhost:${TARGET_PORT}`);
});
