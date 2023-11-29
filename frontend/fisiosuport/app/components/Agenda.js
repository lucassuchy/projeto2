"use client";

export default function Agenda() {
  return (
    <div>
      <div class="container">
        <div class="left">
          <div class="calendar">
            <div class="month">
              <i class="fas fa-angle-left prev"></i>
              <div class="date">Dezembro 2015</div>
              <i class="fas fa-angle-right next"></i>
            </div>
            <div class="weekdays">
              <div>Dom</div>
              <div>Seg</div>
              <div>Ter</div>
              <div>Qua</div>
              <div>Qui</div>
              <div>Sex</div>
              <div>Sab</div>
            </div>
            <div class="days"></div>
            <div class="goto-today">
              <div class="goto">
                <input type="text" placeholder="mm/yyyy" class="date-input" />
                <button class="goto-btn">Go</button>
              </div>
              <button class="today-btn">Hoje</button>
            </div>
          </div>
        </div>
        <div class="right">
          <div class="today-date">
            <div class="event-day"></div>
            <div class="event-date">12 Dezembro 2022</div>
          </div>
          <div class="events"></div>
          <div class="add-event-wrapper">
            <div class="add-event-header">
              <div class="title">Adicionar Evento</div>
              <i class="fas fa-times close"></i>
            </div>
            <div class="add-event-body">
              <div class="add-event-input">
                <input
                  type="text"
                  placeholder="Adicionar título"
                  class="event-name"
                />
              </div>
              <div class="add-event-input">
                <input
                  type="text"
                  placeholder="Horário de início"
                  class="event-time-from"
                />
              </div>
              <div class="add-event-input">
                <input
                  type="text"
                  placeholder="Horário final"
                  class="event-time-to"
                />
              </div>
            </div>
            <div class="add-event-footer">
              <button class="add-event-btn">Salvar</button>
            </div>
          </div>
        </div>
        <button class="add-event">
          <i class="fas fa-plus"></i>
        </button>
      </div>
      <script src="scriptAgenda.js"></script>
    </div>
  );
}
