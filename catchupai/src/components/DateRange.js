import { useRecoilState , RecoilRoot } from 'recoil';
import { dateRangeState } from '../state/DateRangeState'
import * as React from 'react';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { Box } from '@mui/material';
import { DateRangePicker } from '@mui/x-date-pickers-pro/DateRangePicker';
import { convertDate } from '../util';
export default function DateRange() {
  const [dateRange, setDateRange] = useRecoilState(dateRangeState);

  const handleDateChange = (newValue) => {
    setDateRange(newValue);
  };

  return (
    <Box display="flex" justifyContent="center">
      <LocalizationProvider dateAdapter={AdapterDayjs}>
        <DateRangePicker
          localeText={{ start: 'From', end: 'To' }}
          value={dateRange}
          onChange={handleDateChange}
        />
      </LocalizationProvider>
    </Box>
  );
}