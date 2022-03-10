import axios from 'axios'
import { getCookie, setCookie } from './cookies'

export const verifyJWT = async () => {
    let responses = await fetch('http://localhost:8000/server/checkJWT', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'token': getCookie('jwt')})
    })
    responses.status == 200 ? responses = true : responses = false

    return responses
}

export const checkSSO = () => {
    axios.post('https://docs.microsoft.com/en-us/azure/active-directory/develop/id-tokens', )
}

export const createJWT = () => {
    try {
        axios.post('server/getJWT', "username=jwt&password=jwtadmin")
        .then(res => setCookie('jwt', res.data.token, 1))
    } catch (err) {
        console.log(err)
    }

}