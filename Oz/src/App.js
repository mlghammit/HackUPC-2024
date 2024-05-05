import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Splash from "./Splash";
import HelpSelect from "./HelpSelect";
import Map from "./Map";

function App() {
      return (
            <div>
                  <Router>
                        <Routes>
                            <Route exact path='/' element={<Splash/>} />
                            <Route exact path='/HelpSelect' element={<HelpSelect/>} />
                            <Route exact path='/Map' element={<Map/>} />
                        </Routes>
                  </Router>
            </div>
      );
}

export default App;
