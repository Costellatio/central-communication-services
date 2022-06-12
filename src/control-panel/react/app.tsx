import React from 'react';
import ReactDOM from 'react-dom/client';

import BoxCoverCanvas from './box-cover-canvas/box-cover-canvas';

function App() {
  return (
    <BoxCoverCanvas />
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
