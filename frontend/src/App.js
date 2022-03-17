import React from 'react'
import { Route, Routes, Redirect } from 'react-router-dom'
import { Room } from './components/room/Room'
import { Home } from './components/Home'
import { Lobby } from './components/lobby/Lobby'
import { Proccess } from './components/proccessing/Proccess'
import { getCookie } from './functions/cookies'
export const App = () => {
  
  return (
    <>
      <Routes>
        <Route path="/" element={ <Home /> }></Route>
        <Route path="/lobby" element={ <Lobby /> }></Route> 
        <Route path="/room" element={ <Room /> }></Route>
        <Route path="/proccess" element={ <Proccess /> }></Route>
      </Routes>
    </>
  )
}
