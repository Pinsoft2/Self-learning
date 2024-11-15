# Design Document

By Pinsoft

Video overview: <[CS50 SQL Final Proj - Pinsoft](https://youtu.be/xj-XEd-y_VU)>

* Project title: Smart Stove
* Author JJ Zhang
* GitHub username: Pinsoft2
* EdX username: Pinsoft
* MA, US
* Date of recording: 8/2/2024
## Scope

In this section you should answer the following questions:

* What is the purpose of your database?

I have been always interested in a startup involves smart stoves that basically have a camera looking over the cooking status over the stove in a household, and allows the system to adjust the stove as needed. These stoves are equipped with cameras that monitor cooking status and adjust the stove's settings as needed. This innovation aims to enhance safety and convenience in the kitchen, preventing overcooking or burning food by automatically managing stove operations.

* Which people, places, things, etc. are you including in the scope of your database?

    1. Users information that records the buyer basic info, house address, IP address, wifi password, dates of purchase and installment, Camera id, switch id;
    2. Cameras table should contain camera id, manufactured date, internet status, scanning id, user id and switch id;
    3. Scannings should be live updated with stove status, camera id, camera internet status and timestamps;
    4. Switches that belong to the stove and directly control the switches, it should list out the related camera id, user id, quantifiable status that represents heat level from 0-9 where 0 means off.

* Which people, places, things, etc. are *outside* the scope of your database?

We don't plan to collect, store, nor use any sensitive personal data, such as:

    * User's bank account records
    * Birthday
    * Identity number

Business operational data are excluded as well, such as:
    * Price
    * Cost
    * Manufactured date
    * Insurance policy

## Functional Requirements

In this section you should answer the following questions:

* What should a user be able to do with your database?

    1. Register and deactivate their account
    2. View and update their personal information
    3. Add, remove, or update information about their smart stove system (camera, switch)
    4. View real*time stove status and scanning information
    5. Adjust stove settings remotely
    6. View historical cooking data and patterns


* What's beyond the scope of what a user should be able to do with your database?

    1. Access or modify other users' information
    2. Directly manipulate raw scanning data
    3. Modify camera or switch hardware information
    4. Access or modify business operational data
    5. Extract or export large datasets

## Representation

### ERD diagram:
![ERD](final%20proj%20ERD.jpg)

### Entities

In this section you should answer the following questions:


* Which entities will you choose to represent in your database?

    * Users
    * Cameras
    * Scannings
    * Switches


* What attributes will those entities have?

    * Users:
        * UserID (Primary Key)
        * Name
        * Email
        * HomeAddress
        * IPAddress
        * WiFiPassword
        * PurchaseDate
        * InstallationDate
        * CameraID (ForeignKey)
        * SwitchID (ForeignKey)

    * Cameras:
        * CameraID (Primary Key)
        * ManufacturedDate
        * InternetStatus
        * UserID (ForeignKey)
        * ScanningID (ForeignKey)
        * SwitchID (ForeignKey)

    * Scannings:
        * ScanningID (Primary Key)
        * CameraID (Foreign Key)
        * Timestamp
        * StoveStatus
        * image

    * Switches:
        * SwitchID (Primary Key)
        * CameraID (Foreign Key)
        * UserID (Foreign Key)
        * HeatLevel (0-9)   <- ENUM

* Why did you choose the types you did?

    * User ID, Camera ID, Scanning ID, Switch ID: These are unique identifiers necessary to uniquely distinguish each record.

    * Name, Email, Address: Essential personal information for user identification and communication.

    * IP Address, Wifi Password: Needed for connecting and managing the smart devices.
    Manufactured Date, Internet Status: Important for tracking the state and condition of cameras.

    * Stove Status, Timestamp: Critical for monitoring the cooking process.
    Heat Level: Represents the state of the stove’s heat, crucial for the functioning of smart stoves.

* Why did you choose the constraints you did?

    * Primary Keys: To ensure each entity can be uniquely identified.

    * Foreign Keys: To establish relationships between entities and ensure data integrity.

    * Data Types: Selected to match the nature of the data (e.g., timestamps for recording time, integers for IDs and heat levels).


### Relationships

In this section you should include your entity relationship diagram and describe the relationships between the entities in your database.

* Relationship Descriptions*
    * Users to Cameras: One-to-Many relationship where one user can have multiple cameras.
    * Users to Switches: One-to-Many relationship where one user can have multiple switches.
    * Cameras to Scannings: One-to-Many relationship where one camera can generate multiple scanning records.
    * Cameras to Switches: One-to-One relationship where each camera is associated with a single switch.
    * Switches to Users: Many-to-One relationship where multiple switches can be controlled by one user.


## Optimizations

In this section you should answer the following questions:

* Which optimizations (e.g., indexes, views) did you create? Why?

Indexes:

Created on User ID, Camera ID, Switch ID to speed up queries involving these keys.
Index on Timestamp in the Scannings table to accelerate time-based queries.

Views:

Created views to simplify complex queries, such as a combined view of stove status with user information.
A view for active cameras and their status to quickly monitor the operational state of the system.


## Limitations

In this section you should answer the following questions:

* What are the limitations of your design?

    * Scalability: As the number of users, cameras, and switches grows, performance may degrade without further optimization.

    > The current design doesn't account for multiple stoves per user. It may not scale well for users with very large numbers of historical scans. The design also doesn't include a way to group or categorize different cooking sessions.

    * Real-time Updates: The system may face delays in real-time updates due to network or processing latencies.

    * Data Privacy: Although personal data is minimized, ensuring complete security and privacy remains challenging.

* What might your database not be able to represent very well?

    * Complex User Preferences: Detailed user preferences and cooking patterns may not be effectively captured.

    * Hardware Faults: The system may not accurately represent hardware faults or require additional diagnostics outside the database’s scope.

    * Dynamic Configurations: Rapid changes in stove configurations and user interactions may be difficult to track in real-time.
