import React from 'react'
import Search from './Search'


const Hero = () => {

  return (
    <div className='absolute top-[15%] flex flex-col text-green p-4'> 
    <div className=' flex flex-col w-60'>
      <h2 className='text-3xl text-center text-green'> Turn your daily tasks into code! </h2>
      <h1 className='font-italic font-thin text-blue-950 text-center'>
        This tool hooks you up with explanations, pseudocode, and Python code for whatever you're tackling in your day-to-day life</h1>
        </div>
      <div>
        <form className='search'>
        <div className='py-5'>
        <Search />
        </div>
      </form>
    </div>
    </div>


  
   
 
  )
}

export default Hero