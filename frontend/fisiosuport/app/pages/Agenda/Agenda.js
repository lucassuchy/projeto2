import React, { useState } from 'react';
import { startOfMonth, endOfMonth, addMonths, eachDayOfInterval, format } from 'date-fns';

const Calendar = () => {
  const [events, setEvents] = useState([]);
  const [newEvent, setNewEvent] = useState('');
  const [selectedDate, setSelectedDate] = useState(null);
  const [currentDate, setCurrentDate] = useState(new Date());

  const handleDayClick = (day) => {
    setSelectedDate(day);
  };

  const handleAddEvent = () => {
    if (selectedDate && newEvent.trim() !== '') {
      const updatedEvents = [...events, { date: selectedDate, event: newEvent }];
      setEvents(updatedEvents);
      setNewEvent('');
      setSelectedDate(null);
    }
  };

  const handleRemoveEvent = (date) => {
    const updatedEvents = events.filter((event) => event.date !== date);
    setEvents(updatedEvents);
  };

  const handlePrevMonth = () => {
    setCurrentDate(addMonths(currentDate, -1));
  };

  const handleNextMonth = () => {
    setCurrentDate(addMonths(currentDate, 1));
  };

  const renderCalendar = () => {
    const days = eachDayOfInterval({ start: startOfMonth(currentDate), end: endOfMonth(currentDate) });

    return (
      
      <div className="calendar-header">
          <button onClick={handlePrevMonth}>&lt;</button>
          <h2>{format(currentDate, 'MMMM yyyy')}</h2>
          <button onClick={handleNextMonth}>&gt;</button>
       
      <div className="calendar">
        {days.map((day) => (
          <div
            key={day.toISOString()}
            className={`day ${selectedDate && day.toDateString() === selectedDate.toDateString() ? 'selected' : ''}`}
            onClick={() => handleDayClick(day)}
          >
            {format(day, 'd')}
          </div>
        ))}
      </div>
      </div>
    );
  };

  return (
    <div className="calendar-container">
      <h2>Event Calendar</h2>
      {renderCalendar()}
      <div className="event-input">
        <input
          type="text"
          placeholder="Informe o Evento"
          value={newEvent}
          onChange={(e) => setNewEvent(e.target.value)}
        />
        <button className='adicionar' onClick={handleAddEvent}>Salvar</button>
      </div>
      <div className="events-list">
        <h3>Eventos Agendados</h3>
        <ul>
          {events.map((event, index) => (
            <li key={index}>
              {format(event.date, 'MMMM d, yyyy')} - {event.event}
              <button className='remover' onClick={() => handleRemoveEvent(event.date)}>Remove</button>
            </li>
          ))}
        </ul>
      </div>
      <style>{`
        
        .calendar {
          display: grid;
          grid-template-columns: repeat(7, 1fr);
          gap: 20px;
          max-width: 500px;
          margin: 150px 500px 50px 500px;
          
        }

       .calendar-header h2{
        margin: 150px 50px 0 50px;
        display: inline-block;
        align-items:center;
        
       }

        .day {
          cursor: pointer;
          padding: 30px;
          text-align: center;
          border: 1px solid #fff;
          background-color: #212F3F;
          transition: background-color 0.3s;
        }

        .day:hover {
          background-color: #e0e0e0;
        }

        .day.selected {
          background-color: #a0d3e8;
        }

        .event-input {
          margin-top: 16px;
          display: center;
          justify-content: center;
          align-items: center;
          margin: 0 500px;
        }

                 
        input {
          flex: 1;
          padding: 8px;
          margin-right: 8px;
          color: black;
          border-radius: 4px;
        }

        button {
          padding: 8px;
          background-color: #4caf50;
          color: #fff;
          border-radius: 10px;
          cursor: pointer;
          width: 50px;

        }

        .adicionar {
          padding: 8px;
          background-color: #4caf50;
          color: #fff;
          border-radius: 10px;
          cursor: pointer;
          width: auto;

        }

        .remover {
          padding: 8px;
          background-color: red;
          color: #fff;
          border-radius: 10px;
          cursor: pointer;
          width: auto;

        }


        button:hover {
          background-color: #45a049;
        }

        .events-list {
          margin-top: 24px;
          border: 10px;
          display: center;
        }

        ul {
          list-style: none;
          padding: 0;
        }

        li {
          color: black;
          margin-bottom: 8px;
          padding: 8px;
          border: 1px solid #ddd;
          background-color: #f9f9f9;
          display: flex;
          justify-content: space-between;
          align-items: center;
          border-radius: 7px;
        }

        li button {
          padding: 10px;
          background-color: #f44336;
          color: #fff;
          border: none;
          cursor: pointer;
          border-radius: 5px;
        }

        li button:hover {
          background-color: #d32f2f;
        }
      `}</style>
    </div>
  );
};

export default Calendar;
