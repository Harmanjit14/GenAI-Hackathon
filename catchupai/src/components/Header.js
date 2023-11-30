import React, { useState } from 'react';
import { Toolbar, Typography, Avatar, Input } from '@mui/material';
import Logo from '../logo.svg'; // Import your logo
import dProfile from '../harman.png'
function Header() {
    const [profilePic, setProfilePic] = useState(dProfile);
  
    const handleUpload = (event) => {
      const file = event.target.files[0];
      const reader = new FileReader();
  
      reader.onloadend = () => {
        setProfilePic(reader.result);
      };
  
      reader.readAsDataURL(file);
    };
  
    return (
      <Toolbar>
        <img src={Logo} alt="Logo" style={{ marginRight: 'auto', height: '53px', width: 'auto' }}
        /> 
        <Input
          accept="image/*"
          id="icon-button-file"
          type="file"
          sx={{ display: 'none' }}
          onChange={handleUpload}
        />
        <label htmlFor="icon-button-file">
          <Avatar alt="Profile Picture" src={profilePic} />
        </label>
      </Toolbar>
    );
}
  
export default Header;