import React, {useState, useEffect} from 'react'
import APIService from './APIService'
import { useCookies } from 'react-cookie'
import {useNavigate} from 'react-router-dom'

export default function Login() {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [isLogin, setLogin] = useState(true)
    const [token, setToken] = useCookies(['auth_token'])
    let navigate = useNavigate()


    useEffect(() => {
      if(token['auth_token']){
        navigate('/articles')  // redirects user to the /articles
      }
    }, [token])
    

    const loginBtn = () => {
        APIService.LoginUser({username, password})
        .then(resp => {
          if(resp.token) 
          {setToken("auth_token", resp.token)}
          else {console.error(resp);}
        }
          )
        .catch(error => console.error(error))
    }

    const registerBtn = () => {
      APIService.RegisterUser({username, password})
      .then(resp => console.log(resp))
      .catch(error => console.log(error))
    }

  return (
    <div className="App">
        <div className="container">
            <br /><br />
            {isLogin ? <h1>Please Login</h1> : <h1>Please Register</h1>}
            
            <br /><br />
            
            <div className="mb-3">
                <label htmlFor="username" className="form-label">Username</label>
                <input type="text" className="form-control" id="username" value={username} onChange={e=>setUsername(e.target.value)}  placeholder="Please enter username" />
                <br />

                <label htmlFor="password" className="form-label">Password</label>
                <input type="text" className="form-control" id="password" value={password} onChange={e=>setPassword(e.target.value)} placeholder="Please enter password" />
                <br />


                {isLogin 
                  ? <button onClick={loginBtn} className="btn btn-primary">Login</button>
                  : <button onClick={registerBtn} className="btn btn-primary">Register</button>
                  }
                
                
                <div className="mb-3">
                  <br />
                  {isLogin 
                  ? <h5>If you don't have Account, Please <button className="btn btn-primary" onClick={()=>setLogin(false)}>Register</button> Here</h5>
                  : <h5>If you already have Account, Please <button className="btn btn-primary" onClick={()=>setLogin(true)}>Login</button> Here</h5>
                  }
                </div>
            </div>
        </div>
    </div>
  )
}
