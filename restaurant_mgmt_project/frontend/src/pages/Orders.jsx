import React, {useState, useEffect} from 'react'
import axios from 'axios'
const API = "http://localhost:8000/api"

export default function Orders(){
  const [restaurants, setRestaurants] = useState([])
  const [menu, setMenu] = useState([])
  const [order, setOrder] = useState({restaurant:null, table:null, items:[]})
  const [orders, setOrders] = useState([])

  useEffect(()=>{ fetchRestaurants(); fetchOrders() },[])

  async function fetchRestaurants(){ const r = await axios.get(API+'/restaurants/'); setRestaurants(r.data) }
  async function fetchMenu(restId){ const r = await axios.get(API+`/menu-items/?restaurant=${restId}`); setMenu(r.data) }

  async function createOrder(e){
    e.preventDefault()
    // transform items to expected serializer shape
    const payload = {...order}
    payload.items = order.items.map(it=>({menu_item: it.id, quantity: it.qty}))
    await axios.post(API+'/orders/', payload); setOrder({restaurant:null,table:null,items:[]}); fetchOrders()
  }

  function addItemToOrder(menuItem){ setOrder(prev=>({...prev, items:[...prev.items, {id:menuItem.id, name:menuItem.name, qty:1}]})) }
  function updateQty(idx, val){ const it = [...order.items]; it[idx].qty = Number(val); setOrder({...order, items:it}) }

  async function fetchOrders(){ const r = await axios.get(API+'/orders/'); setOrders(r.data) }

  return <div>
    <h3>Create Order</h3>
    <div>
      <select value={order.restaurant||''} onChange={async e=>{ const id = e.target.value; setOrder({...order,restaurant:id}); fetchMenu(id) }}>
        <option value=''>Select Restaurant</option>
        {restaurants.map(r=> <option key={r.id} value={r.id}>{r.name}</option>)}
      </select>
    </div>
    <div>
      <h4>Menu</h4>
      <ul>{menu.map(m=> <li key={m.id}>{m.name} - ₹{m.price} <button onClick={()=>addItemToOrder(m)}>Add</button></li>)}</ul>
    </div>
    <form onSubmit={createOrder}>
      <h4>Order Items</h4>
      <ul>{order.items.map((it,idx)=> <li key={idx}>{it.name} Qty: <input type="number" value={it.qty} onChange={e=>updateQty(idx,e.target.value)} /></li>)}</ul>
      <button type="submit">Place Order</button>
    </form>
    <hr/>
    <h3>Recent Orders</h3>
    <ul>{orders.map(o=> <li key={o.id}>{o.id} - {o.status} - ₹{o.total}</li>)}</ul>
  </div>
}