import React from 'react'
import {Route, Routes} from 'react-router-dom'

import { Room } from './components/room/Room'
import { Home } from './components/Home'

export const App = () => {
  return (
    <Routes>
      <Route path="/" element={ <Home /> }></Route>
      <Route path="/room" element={ <Room /> }></Route>
    </Routes>
  )
}
