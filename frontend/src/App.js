import React from 'react'
import {Route, Routes} from 'react-router-dom'

import { Room } from './components/room/Room'
import { Home } from './components/Home'

// use context

export const App = () => {
  return (
    <a href="http://localhost:8000/server/signin">Sign in</a>
    // <Routes>
    //   <Route path="/" element={ <Home /> }></Route>
    //   <Route path="/room" element={ <Room /> }></Route>
    // </Routes>
  )
}
