import React, { useEffect, useState } from 'react';
import './styles/Oz.css';
import './styles/Helpselect.css';
import { Link } from "react-router-dom";
import PassScanner from "./PassScanner";

function HelpSelect() {
    const [selectedValue, setSelectedValue] = useState('');
    const [infoPrompt, setInfoPrompt] = useState('');
    const [inputValue, setInputValue] = useState('');
    const [selectValue, setSelectValue] = useState('');

    useEffect(() => {
            determinePrompt();
        },
        [selectedValue]);

    function enableButton() {
        document.getElementById("letsGo").style.display = "block";
        console.log("Button enabled");
    }

    function disableButton() {
        document.getElementById("letsGo").style.display = "none";
        console.log("Button disabled");
    }

    useEffect(() =>{
        enableButton();
        disableButton();
    }, []);
    function determinePrompt() {
        switch (selectedValue) {
            case "Gate":
                setInfoPrompt("My Flight or Gate Number...");
                disableButton()
                break;
            case "Check In":
                setInfoPrompt("I'm travelling with...");
                disableButton();
                break;
            case "Restaurant":
                setInfoPrompt("I want to eat at...");
                disableButton();
                break;
            case "Bathroom":
                setInfoPrompt('');
                enableButton();
                break;
            default:
                setInfoPrompt('');
                break;
        }
    }

    function handleOptionChange(event) {
        setSelectedValue(event.target.value);
        setInputValue('');
        setSelectValue('');
    }

    function handleSelectChange(event, selectId) {
        const value = event.target.value;
        setSelectValue(value);
        enableButton();
        console.log(`Selected value of ${selectId}: ${value}`);
    }

    return (
        <div className="helpSelect center">
            <p>I need help finding...</p>
            <select id="switchBoard" value={selectedValue} onChange={handleOptionChange}>
                <option value="" hidden>Select an option</option>
                <option value="Bathroom">Bathroom</option>
                <option value="Gate">Gate</option>
                <option value="Check In">Check In</option>
                <option value="Restaurant">Restaurant</option>
            </select>

            {infoPrompt && (
                <p className="extras">{infoPrompt}</p>
            )}

            {selectedValue === "Gate" && (
                <input
                    type="text"
                    id="flightGateNo"
                    value={inputValue}
                    onChange={(e) => handleSelectChange(e, "flightGateNo")}
                />
            )}

            {selectedValue === "Check In" && (
                <select
                    id="airlineCarrier"
                    value={selectValue}
                    onChange={(e) => handleSelectChange(e, "airlineCarrier")}
                >
                    <option>Select an airline</option>
                    <option>Airline 1</option>
                    <option>Airline 2</option>
                    <option>Airline 3</option>
                    <option>Airline 4</option>
                </select>
            )}

            {selectedValue === "Restaurant" && (
                <select id="restaurant" value={selectValue} onChange={(e) => handleSelectChange(e, "restaurant")}>
                    <option>Select a restaurant</option>
                    <option>Restaurant 1</option>
                    <option>Restaurant 2</option>
                    <option>Restaurant 3</option>
                    <option>Restaurant 4</option>
                </select>
            )}
            <div id="letsGo">
                <button >LET'S GO!</button>
            </div>

            <h2>OR</h2>

            <Link to="/PassScanner"><button>SCAN BOARDING PASS</button></Link>
        </div>
    );
}

export default HelpSelect;
