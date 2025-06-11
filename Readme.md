# IoT Smart Vehicle System - Software Requirements Specification (SRS)

## Document Version
**Version:** 2.0

---

## Table of Contents
1. [Purpose](#1-purpose)  
    1.1. [Intended Audience](#11-intended-audience)  
    1.2. [Intended Use](#12-intended-use)  
    1.3. [Scope](#13-scope)  
    1.4. [Definitions and Acronyms](#14-definitions-and-acronyms)  
2. [Overall System Description](#2-overall-system-description)  
    2.1. [Use Case Diagrams](#21-use-case-diagrams)  
    2.2. [System Architecture](#22-system-architecture)  
    2.3. [Functional Requirements](#23-functional-requirements)  
        - 2.3.1. [Start Up and Main Interface](#231-start-up-and-main-Interface)  
        - 2.3.2. [Door locking and power status mechanisms](#232-door-locking-and-power-status-mechanisms)  
        - 2.3.3. [Start Engine](#233-start-engine)  
        - 2.3.4. [Stop Engine](#234-stop-engine)  
        - 2.3.5. [Driving Mode Selection](#235-driving-ode-election)  
        - 2.3.6. [Environment Monitoring](#236-environment-monitoring)  
	- 2.3.7. [Function Remote Access via Mobile App](#237-function-remote-access-via-mobile-app)  
        - 2.3.8. [Authentication Services](#238-authentication-services)  
        - 2.3.9. [User Management](#239-user-management)  
        - 2.3.10. [Intrusion Detection and Notification](#2310-intrusion-detection-and-notification)  
    2.4. [Non-Functional Requirements](#24-non-functional-requirements)  
	- 2.4.1. [Non-Functional Requirement for Power Status Conditions](#241-non-functional-requirement-for-power-status-conditions)
	- 2.4.2. [Non-Functional Requirement for Performance](#242-non-functional-requirement-for-performance)
 	- 2.4.3. [Non-Functional Requirement for Connectivity](#243-non-functional-requirement-for-connectivity)
  	- 2.4.4. [Non-Functional Requirement for Reliability](#244-non-functional-requirement-for-reliability)
  	- 2.4.5. [Non-Functional Requirement for Environmental](#245-non-functional-requirement-for-environmental)
  	- 2.4.6. [Non-Functional Requirement for Security](#246-non-functional-requirement-for-security)
  	- 2.4.7. [Non-Functional Requirement for Maintainability](#247-non-functional-requirement-for-maintainability)
3. [Software Architecture](#3-software-architecture)  
    3.1. [Static Software Architecture](#31-static-software-architecture)  

---

## 1. Purpose
## 	1.1 Intended Audience
This SRS document describes the System Requirements and Software Design for a vehicle security and telematics system and the target audience are System and Software Engineers working on the development of this project.

## 1.2 Intended Use
The SRS defines the overall System Architecture and Requirements as well as the Software Architecture and Design. This document also contains the definition of the System Requirements which shall be used as the input for System Test cases and Software Unit Test cases

## 1.3 Scope
This Software Requirements Specification (SRS) document outlines the functional and non-functional requirements of a Vehicle Security and Telematics System. It also defines the scope of both the system-level and software-level design, offering a comprehensive framework to guide system development, integration, and testing. The system is designed to enhance vehicle safety, monitor real-time data, and provide remote access and control features.

## 1.4 Definitions and Acronyms

| Acronym | Description |
|--------|-------------|
| IR | Infrared Sensor |
| LED | Light Emitting Diode |
| LCD | Liquid Crystal Display |
| LDR | Light Dependent Resistor |
| RFID | Radio Frequency Identification |
| RainSens | Moisture Sensor |
| USONIC | Ultrasonic Sensor |
| Servo Motor | Angular position motor |
| DC Motor | Rotational electric motor |
| THS | Temperature and Humidity Sensor |
| Sensor (General) | Environmental or condition detector |
| AC | Air Conditioning |


## 2. Overall System Description



## 2.1 Use Case Diagrams



## 2.2 System Architecture



## 2.3 Functional Requirements

### 2.3.1. Start Up and Main Interface
This section defines the functional requirements related to the system's behaviour during startup and navigation through the main and idle menu. It includes conditions for accessing features via the LCD interface, RFID authentication, and internet connection to mobile application.

| REQ_ID | Requirement |
|--------|-------------|
| **REQ-01** | When the smart vehicle is powered ON, after completing RFID authentication, the main menu with the following text shall be displayed on the LCD screen:  <br> Line 1 = “1. Initialize the vehicle” <br> Line 2 = “2. Lock/Unlock Door” |
| **REQ-02** | If “1. Initialize the vehicle” from REQ-01 is selected by pressing 1 on keypad, and a valid RFID card has been scanned, the LCD shall display the idle menu:  <br> **Page 1**: <br> Line 1 = “1. Start/Stop Engine” <br> Line 2 = “2. Lock/Unlock Door” <br> **Page 2**: <br> Line 1 = “3. Check Sensors” <br> Line 2 = “4. Initialise Mobile Connection” <br> **Page 3**: <br> Line 1 = “5. Low power mode” <br> Line 2 = “6. Power off” |


### 2.3.2. Door Locking and Power Status Mechanisms
This section defines the conditions for enabling the locking door mechanisms, as well as enabling low power mode or powering off the vehicle. It also defines how the system behaves and returns to original operation from these power status mechanisms.

| REQ_ID  | Requirement |
|--------|-------------|
| **REQ-03** | When the LCD is displaying either the Main Menu or Page 1 of the Idle Menu (as defined in REQ-02), and the user selects option "2. Lock/Unlock Door" either:<br>- by pressing key 2 on the keypad, or<br>- through the mobile app<br><br>The system shall:<br>1. Activate the door locking mechanism.<br>2. Display the following text on the LCD for 2 seconds:<br>&nbsp;&nbsp;&nbsp;&nbsp;a. Line 1: "Doors Locked"<br><br>After the message is displayed, the LCD shall return to the previously displayed menu. |
| **REQ-04** | When the engine is idle, and the user selects the “5. Low power mode” option either by:<br>- Pressing keypad key 5 while the LCD displays Idle Menu – Page 3, or<br>- Selecting the corresponding option via the mobile app<br><br>The system shall:<br>1. Turn off the LCD backlight.<br>2. Activate the door locking mechanism.<br>3. Disable all functions except:<br>&nbsp;&nbsp;&nbsp;&nbsp;a. the mobile app connection module<br>&nbsp;&nbsp;&nbsp;&nbsp;b. the vehicle intrusion detection function<br><br>The system shall remain in low power mode until:<br>- any keypad button is pressed, or<br>- a deactivation command is received via the mobile app.<br><br>**Non-Functional:** The system shall enter low power mode within 1 second of activation. |
| **REQ-05** | When the engine is idle and the LCD is displaying Page 3 of the Idle Menu (REQ-02), and the user selects "6. Power off" either:<br>- by pressing key 6 on the keypad, or<br>- through the mobile app<br><br>The system shall:<br>1. Disable all functions except:<br>&nbsp;&nbsp;&nbsp;&nbsp;a. connection to the mobile app<br>&nbsp;&nbsp;&nbsp;&nbsp;b. vehicle intrusion detection<br>2. Return the display to the Main Menu on the LCD.<br><br>**Non-Functional:** This mode shall only be activated if the engine is idle. |


### 2.3.3. Start Engine

…
 
### 2.3.4. Stop Engine

...

### 2.3.5. Driving Mode Selection

...

### 2.3.6. Environment Monitoring

...

### 2.3.7. Function Remote Access via Mobile App

...

### 2.3.8. Authentication Services

...

### 2.3.9. User Management

…

### 2.3.9. Intrusion Detection and Notification

…

## 2.4 Non-Functional Requirements

### 2.4.1.Non-Functional Requirement for Power Status Conditions

... 

### 2.4.2. Non-Functional Requirement for Performance

... 

### 2.4.3. Non-Functional Requirement for Connectivity

... 

### 2.4.4. Non-Functional Requirement for Reliability

... 

### 2.4.5. Non-Functional Requirement for Environmental

... 

### 2.4.6. Non-Functional Requirement for Security

... 

### 2.4.7. Non-Functional Requirement for Maintainability

...

## 3. Software Architecture

...

### 3.1 Static Software Architecture

…

---

> 🛠 This documentation is part of an IoT-based smart vehicle security and telematics project developed for educational and research purposes.
