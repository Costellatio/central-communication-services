import React, { useEffect, useState } from 'react';

interface Position {
  x: number,
  y: number,
  z: number,
}

const DEFAULT_POSITION = {
  x: 0,
  y: 0,
  z: 0,
};

const socket = new WebSocket('ws://localhost:3030');

socket.addEventListener('open', function (event) {
  console.log('conn establisherd');
  socket.send('Connection Established');
});

socket.addEventListener('message', function (event) {
  console.log(event.data);
});

function BoxCoverCanvas() {
  const [position, setPosition] = useState<Position>(DEFAULT_POSITION);

  useEffect(() => {
    const canvas = document.getElementById('box-cover-canvas') as HTMLCanvasElement;
    const context = canvas.getContext('2d');

    function resize() {
      canvas.width  = window.innerWidth;
      canvas.height = window.innerHeight;

      draw();
    }

    function draw() {
      context.beginPath();
      context.moveTo(window.innerWidth / 4, window.innerHeight / 2);
      context.lineTo(window.innerWidth / 4, 150);
      context.strokeStyle = 'black';
      context.lineWidth = 2;
      context.stroke();
    }

    resize();

    window.addEventListener('resize', resize);
    return () => {
      window.removeEventListener('resize', resize);
    };
  });

  useEffect(() => {
    console.log(position);
  }, [position]);

  return (
    <canvas id='box-cover-canvas' />
  );
}

export default BoxCoverCanvas;
