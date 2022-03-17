import React, {useEffect, useState, useContext} from 'react'
import { Link, Navigate  } from 'react-router-dom'
import style from './lobby.module.css'
import axios from 'axios'
import { setCookie, getCookie } from '../../functions/cookies'

export const Lobby = () => {

  const [ username, setusername ] = useState('')

  useEffect( async () => {
      const username1 = getCookie('username').replace('"', '').replace('"', '')
      setusername( username1 )
  }, [])

  const saveRoomNameToCookie = () => {
    setCookie('room_name', room_name.value, 1)
  }

  const logout = () => {
    setCookie('username', '', 1)
    setCookie('jwt', '', 1)
    setCookie('room_name', '', 1)
    axios.get('/server/signout')
  }

  return (
    <div>
        <Link
         to='/'
         onClick={logout}
         > Log Out </Link>
        <h1> {username} </h1>
        <form  className={style.container}>
        <label htmlFor='room_name'> Room Name </label>
        <input type='text' id='room_name' placeholder='Room Name' required />
        <Link
          to='/room'
          onClick={ e => saveRoomNameToCookie(e)}
          > <button> Enter Room </button>
        </Link>
      </form>
    </div>
  )
}
