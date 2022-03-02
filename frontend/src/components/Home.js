import React, {useEffect} from 'react'
import axios from 'axios'

export const Home = () => {
  
  const headers = {"X-CSRFTOKEN": "nosniff"};

  const enterRoom = (e) => {
    e.preventDefault()
    const formData = {
      room: room_name.value,
      username: user_name.value
    }

    axios.post('http://localhost:8000/server/checkroom/', JSON.stringify(formData))
      .then(data => 
        window.location.href = `http://localhost:8000/room/?room=${data.data.room}&name=${data.data.username}`)
  }

  return (
    <form>
      <label htmlFor='room_name'> Room Name </label>
      <input type='text' id='room_name' placeholder='Room Name' />
      <label htmlFor='user_name'> User Name </label>
      <input type='text' id='user_name' placeholder='Name`' />
      <input onClick={enterRoom} type='submit' />
    </form>
  )
}
