import React, {useEffect, useState} from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'
import { Message } from './Message'
import style from './room.module.css'
import { getCookie } from '../../functions/cookies'

const url = `ws://${window.location.host}/ws/socket-server/`
const socket = new WebSocket(url)

export const Room = () => {
  
  const [ messages, setMessages ] = useState([]) 
  const [ roomData, setRoomData ] = useState({})

  useEffect( () => {
    const data = {
      room: getCookie('room_name'),
      username: getCookie('username')
    }
    setRoomData(data)

    try {
      axios.post('/server/checkroom', data)
      axios.post('/server/getMessages/', data)
      .then(res => {
        setMessages(res.data.messages)
      })

      socket.onmessage = (e) => {
        let data = JSON.parse(e.data)
        if(data.type == 'chat') {
          setMessages(messages => [...messages, data]) // react update ...?
        }
      }
    } catch (err) {
      console.log(err)
    }
  }, [])


  const send = (e) => {
    const jwt = getCookie('jwt')
    e.preventDefault()
    let sent = {
      room: roomData.room,
      // username: roomData.username,
      message: room_message.value,
      token: jwt
    }
    socket.send(JSON.stringify(sent))
    axios.post('/server/send', sent)
    .then(res => 
      res.data == 'jwt not found' ? window.location.href = '/' : room_message.value = '')
  }

  return (
    <section className={style.container}>
      <Link to='/lobby'> 
        <button>  back </button>
      </Link>
      
      <h1> {roomData.room} </h1>

      <form>
        <input type="text" id='room_message' placeholder="message" />
        <button onClick={send} type="submit">Send</button>
      </form>
      {messages ? (<Message messages={messages} />) : (<h1>No messages</h1>)}
    </section>
  )
}

// the whole problem of getting lots of responses was due to bad planning
// react was re rendering the whole component on every message