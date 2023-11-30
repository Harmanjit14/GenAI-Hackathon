import React from 'react';
import { Typography } from '@mui/material';


const TextComponent = () => {

  return (
    <Typography  variant="h5" component="div" 
    sx={{ 
      flexGrow: 1, 
      color: '#6e7c7c', 
      textAlign: 'center', 
      margin: '20px 0', 
      fontFamily: 'sans-serif', 
      fontSize: '24px' 
    }}>
    Your AI assistant for a smooth return to work. Pick the time range for your catching up  and regain your momentum!
    </Typography>
  );
};

export default TextComponent;
