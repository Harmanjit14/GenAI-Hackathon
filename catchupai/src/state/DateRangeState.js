import { atom } from 'recoil';

export const dateRangeState = atom({
  key: 'dateRangeState', // unique ID (with respect to other atoms/selectors)
  default: [null, null], // default value
});
