import React, {useEffect, useState} from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import { Message } from './Message'

const url = `ws://${window.location.host}/ws/socket-server/`
const socket = new WebSocket(url)


export const Room = () => {
  
  const [ messages, setMessages ] = useState([]) 
  const [ roomName, setRoomName ] = useState('')
  const [ username, setusername ] = useState('')
  
  useEffect( () => {

    const queryString = window.location.search;
    let data = queryString.split('&')
    data = {
      room: data[0].split('=')[1],
      username: data[1].split('=')[1]
    }

    setusername(data.username)
    setRoomName(data.room)
    
    axios.post('/server/getMessages/', data)
    .then(res => setMessages(res.data.messages) )
  }, [])

  useEffect( () => {
    socket.onmessage = (e) => {
      let data = JSON.parse(e.data)
      console.log(data)
      if(data.type == 'chat') {
        setMessages(messages => [...messages, data]) // react update ...?
      }
    }
  }, [])


  // problem is that onmessage is running nth ammount of times
  // it needs to run only one time on server send

  const send = async (e) => {
    e.preventDefault()
    const data = {
      room: roomName,
      username: username,
      message: e.target.parentElement.text.value
    }

    socket.send(JSON.stringify(data))
    axios.post('/server/send/', data)
    e.target.parentElement.text.value = ''
  }


  

  return (
    <>
      <Link to='/'> Home </Link>
      <h1> {roomName} </h1>
      <form>
        <input type="text" id='text' placeholder="message" />
        <button onClick={send} type="submit">Send</button>
      </form>
      {messages.length > 0 ? (<Message messages={messages} />) : (<h1>No messages</h1>)}
    </>
  )
}

// the whole problem of getting lots of responses was due to bad planning
// react was re rendering the whole component on every message