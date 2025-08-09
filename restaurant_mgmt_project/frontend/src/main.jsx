import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import Home from './pages/Home'
import Dashboard from './pages/Dashboard'
import Orders from './pages/Orders'

function App(){
  return <BrowserRouter>
    <div style={{padding:10,fontFamily:'Arial'}}>
      <h2>Restaurant Management</h2>
      <nav><Link to="/">Home</Link> | <Link to="/dashboard">Dashboard</Link> | <Link to="/orders">Orders</Link></nav>
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/dashboard" element={<Dashboard/>} />
        <Route path="/orders" element={<Orders/>} />
      </Routes>
    </div>
  </BrowserRouter>
}
createRoot(document.getElementById('root')).render(<App/>)