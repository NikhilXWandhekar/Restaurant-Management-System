import React, {useState, useEffect} from 'react'
import axios from 'axios'

const API = "http://localhost:8000/api"

export default function Dashboard(){
  const [restaurants, setRestaurants] = useState([])
  const [menu, setMenu] = useState([])
  const [newRest, setNewRest] = useState({name:'',address:'',phone:''})

  useEffect(()=> fetchRestaurants(), [])

  async function fetchRestaurants(){
    const r = await axios.get(API+'/restaurants/'); setRestaurants(r.data)
  }
  async function createRestaurant(e){
    e.preventDefault()
    await axios.post(API+'/restaurants/', newRest); setNewRest({name:'',address:'',phone:''}); fetchRestaurants()
  }
  return <div>
    <h3>Dashboard</h3>
    <form onSubmit={createRestaurant}>
      <input placeholder="Name" value={newRest.name} onChange={e=>setNewRest({...newRest,name:e.target.value})} required />
      <input placeholder="Phone" value={newRest.phone} onChange={e=>setNewRest({...newRest,phone:e.target.value})} />
      <button type="submit">Add Restaurant</button>
    </form>
    <hr/>
    <h4>Restaurants</h4>
    <ul>{restaurants.map(r=> <li key={r.id}>{r.name} - {r.phone}</li>)}</ul>
  </div>
}