import React from 'react';
import { useRecoilValue } from 'recoil';
import { dateRangeState } from '../state/DateRangeState';
import { ApolloClient, InMemoryCache, gql } from '@apollo/client';
import { convertDate } from '../util';
function Webx() {
  const dateRange = useRecoilValue(dateRangeState);

  const handleClick = async () => {
    const client = new ApolloClient({
      uri: 'https://4438-2001-420-c0e0-1007-00-822.ngrok-free.app/',
      cache: new InMemoryCache(),
    });
     let from , to ;
    if (dateRange[0] !=null){ from=convertDate(dateRange[0].toString())}
    else{ from = null}
    if (dateRange[1] !=null){ to=convertDate(dateRange[1].toString())}
    else {to = null}
    console.log(from);

    // const response = await client.query({
    //   query: gql`
    //     {
    //       getMails(username: "username", password: "password", from_date: "${from}", to_date: "${to}") {
            
    //       }
    //     }
    //   `,
    // });

    // console.log(response.data);
  };

  return (
    <div style={{ margin: '20px' }}>
       It's for webx
    </div>
  );
}

export default Webx;