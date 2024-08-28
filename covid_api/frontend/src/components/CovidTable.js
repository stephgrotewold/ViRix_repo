import React from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';

function CovidTable({ data }) {
  return (
    <TableContainer component={Paper} style={{ marginTop: 20 }}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Country</TableCell>
            <TableCell align="right">Total Cases</TableCell>
            <TableCell align="right">New Cases (Last 7 Days)</TableCell>
            <TableCell align="right">Total Deaths</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data.map((row) => (
            <TableRow key={row.id}>
              <TableCell component="th" scope="row">
                {row.name}
              </TableCell>
              <TableCell align="right">{row.cases_cumulative_total}</TableCell>
              <TableCell align="right">{row.cases_newly_reported_last_7_days}</TableCell>
              <TableCell align="right">{row.deaths_cumulative_total}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}

export default CovidTable;