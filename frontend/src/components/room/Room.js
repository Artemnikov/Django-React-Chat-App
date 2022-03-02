import React, {useEffect, useState} from 'react'
import axios from 'axios'

import { Message } from './Message'

export const Room = () => {

  const [messages, setMessages ] = useState([]) 
  const [ roomName, setRoomName ] = useState('')
  const [ username, setusername ] = useState('')


  // useEffect( async () => {
  //   const queryString = window.location.search;
  //   let data = queryString.split('&')
  //   data = {
  //     room: data[0].split('=')[1],
  //     username: data[1].split('=')[1]
  //   }
  //   setusername(data.username)
  //   setRoomName(data.room)
  //   await axios.post('/server/getMessages/', data)
  //   .then(res => setMessages(res.data.messages) )
  // }, [])

  useEffect( async () => {
    const url = `ws://${window.location.host}/ws/socket-server/`

    const chatSOcket = new WebSocket(url)

    chatSOcket.onmessage = (e) => {
      let data = JSON.parse(e.data)
      console.log(data)
    }
  }, [])
  
  const send = async (e) => {
    e.preventDefault()
    const data = {
      username: username,
      room: roomName,
      message: e.target.parentElement.text.value
    }
    axios.post('/server/send/', data)
  }
  return (
    <>
      <h1> {roomName} </h1>
      {messages.length > 0 ? (<Message messages={messages} />) : (<h1>No messages</h1>)}
      <form>
        <input type="text" id='text' placeholder="message" />
        <button onClick={send} type="submit">Send</button>
      </form>
    </>
  )
}

