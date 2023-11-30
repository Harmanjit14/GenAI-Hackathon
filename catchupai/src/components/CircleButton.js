import React, { useState } from 'react';
import { useRecoilValue } from 'recoil';
import { dateRangeState } from '../state/DateRangeState';
import { ButtonBase, Avatar, Dialog } from '@mui/material';
import Bitbucket from './Bitbucket'; // Import the Bitbucket component
import Mail from './Mail';
import Webx from './Webx';
function CircleButton({ logoPath, logoString }) {
  const dateRange = useRecoilValue(dateRangeState);
  const [open, setOpen] = useState(false);
  const [openMail, setMailOpen] = useState(false);
  const [openWebx, setWebxOpen] = useState(false);
  const handleClick = () => {
    console.log(logoString);
    console.log('Date Range:', dateRange);

    if (logoString === 'bucket') {
      setOpen(true);
    }
    else if(logoString == 'mail') {
        setMailOpen(true)
    }
    else if(logoString == 'webx') {
        setWebxOpen(true)
    }
  };

  const handleClose = () => {
    setOpen(false);
  };

  const handleMailClose = () => {
    setMailOpen(false);
  };
  const handleWebxClose = () => {
    setWebxOpen(false);
  };


  return (
    <>
      <ButtonBase onClick={handleClick} style={{ borderRadius: '50%', overflow: 'hidden' }}>
        <Avatar alt="Logo" src={logoPath} style={{ width: 280, height: 280 }} />
      </ButtonBase>

      <Dialog open={open} onClose={handleClose}>
        <Bitbucket />
      </Dialog>
      
      <Dialog open={openMail} onClose={handleMailClose}>
        <Mail />
      </Dialog>

            
      <Dialog open={openWebx} onClose={handleWebxClose}>
        <Webx />
      </Dialog>

    </>
  );
}

export default CircleButton;