
export const convertDate = (date)=>{
  const originalDate = new Date(date);
  const year = originalDate.getUTCFullYear();
  const month = (originalDate.getUTCMonth() + 1).toString().padStart(2, '0'); // Months are zero-based
  const day = originalDate.getUTCDate().toString().padStart(2, '0');

  const formattedDate = `${year}-${month}-${day}`;
  return formattedDate;
}