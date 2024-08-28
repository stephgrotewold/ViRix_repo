import React from 'react';
import { TextField, Button, Box } from '@mui/material';

function LocationForm({ location, setLocation, fetchData }) {
  return (
    <Box component="form" noValidate autoComplete="off" style={{ marginTop: 20 }}>
      <TextField
        label="Enter Location"
        variant="outlined"
        value={location}
        onChange={(e) => setLocation(e.target.value)}
        style={{ marginRight: 10, width: '300px' }}
      />
      <Button
        variant="contained"
        style={{ backgroundColor: '#007bff', color: '#fff' }}
        onClick={() => fetchData(location)}
      >
        Search
      </Button>
    </Box>
  );
}

export default LocationForm;