import React, {useEffect, useState} from 'react';
import HelpSelect from './HelpSelect';
import { Link, useNavigate } from 'react-router-dom';
import './styles/Oz.css';
import './styles/Splash.css';

function Splash() {
    const navigate = useNavigate()

    useEffect(() => {
        setTimeout(() => {
            navigate("/HelpSelect")
        }, 7000)
    }, [])

    return(
        <div className="splash center">
            <h1> Oz </h1>
            <img src={process.env.PUBLIC_URL + '/assets/logo.png'} alt="Logo" />
            <p>Your Magical Guide</p>
        </div>
    );
}

export default Splash;