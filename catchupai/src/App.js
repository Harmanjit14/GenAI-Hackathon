import './App.css';
import Header from './components/Header';
import DateRange from './components/DateRange';
import {RecoilRoot } from 'recoil';
import Bitbucket from './components/Bitbucket';
import TextComponent from './components/TextComponent';
import CircleButton from './components/CircleButton';
function App() {
  return (
    <RecoilRoot>
      <div className="App">
        <Header />
        <TextComponent/>
        <DateRange/>
        <div style={{ marginTop:150}}>
          <CircleButton logoPath="/outlook.jpg" logoString="mail"/>
          <CircleButton logoPath="/bb.jpg" logoString="bucket" />
          <CircleButton logoPath="/webx.jpeg" logoString="webx" />
        </div>
      </div>
    </RecoilRoot>
  );
}

export default App;
