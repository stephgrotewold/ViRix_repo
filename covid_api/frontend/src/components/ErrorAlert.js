import React from 'react';
import { Alert } from '@mui/material';

function ErrorAlert({ error }) {
  return (
    <Alert severity="error" style={{ marginTop: 20 }}>
      {error}
    </Alert>
  );
}

export default ErrorAlert;