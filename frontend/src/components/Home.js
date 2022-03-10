import React from 'react'
import axios from 'axios'
import style from './Home.module.css'

export const Home = () => {


  return (
    <div className={style.container}>
      <a href="http://localhost:8000/server/signin">Sign in</a>
    </div>
  )
}
