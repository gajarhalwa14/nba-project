# NBA App Current Architecture

This document captures the **current implemented architecture** of the project as it exists in the repository today.

## High-Level Layout

- `backend/` contains the Flask API and data models.
- `frontend/` contains a React + Vite single-page app.
- `IDEAS.md` contains product/UI direction for upcoming work.
- `nba_stats_project_structure.md` describes a more advanced target architecture, but it does **not** match the current code structure yet.

## Backend Architecture (`backend/`)

### Runtime Entry

- `backend/app.py` is the server entry point.
- It imports `app` from `backend/app/__init__.py` and runs Flask in debug mode.

### App Initialization

- `backend/app/__init__.py` initializes:
  - `Flask`
  - `SQLAlchemy` (`db`)
  - `Marshmallow` (`ma`)
- Config is loaded from `backend/config.py`.
- Models and routes are imported at the end to register tables/routes.

### Configuration

- `backend/config.py` uses `python-dotenv` and loads `config.env`.
- Key config:
  - `SQLALCHEMY_DATABASE_URI` from `DATABASE_URL`
  - `DEBUG` from env
  - `SQLALCHEMY_TRACK_MODIFICATIONS = False`

### Data Layer

- `backend/app/models.py` defines SQLAlchemy models for schema `nba_data`:
  - `Player`
  - `Game`
  - `Totals`
  - `GameByGame`
  - `UpcomingGame`
- Models currently live in a single file (not split by domain yet).

### Serialization Layer

- `backend/app/schema.py` defines Marshmallow schemas:
  - `PlayerSchema`
  - `GameSchema`
  - `GameByGameSchema`
  - `TotalsSchema`
  - `UpcomingGameSchema`
- Exposes both single and `many=True` schema instances for route usage.

### API Layer

- `backend/app/routes.py` defines Flask routes directly on `app`.
- CORS enabled for `/api/*`.
- Current API surface:
  - `GET /api/player`
  - `GET /api/players/<id>`
  - `GET /api/search?name=...`
  - `GET /api/game`
  - `GET /api/games/<id>`
  - `GET /api/players/<player_id>/game`
  - `GET /api/players/<player_id>/games/<date>`
  - `GET /api/player/total`
  - `GET /api/players/<id>/totals`
  - `GET /api/upcoming_game`

### Backend Notes

- Current backend uses a straightforward monolithic module pattern (`models.py`, `routes.py`, `schema.py`).
- There is no app-factory + blueprint split yet.
- No tests or migrations directory currently present in this repo layout.

## Frontend Architecture (`frontend/`)

### Tooling and Runtime

- React 19 + Vite 8.
- Main dependencies:
  - `react`
  - `react-dom`
  - `@tanstack/react-query`
- Scripts:
  - `npm run dev`
  - `npm run build`
  - `npm run lint`
  - `npm run preview`

### App Bootstrap

- `frontend/src/main.jsx` is the entry point.
- App is wrapped in a `QueryClientProvider` with a single `QueryClient`.

### Current UI Structure

- `frontend/src/App.jsx` is still template-style and currently acts as one main page.
- There is no route-based page structure yet (no React Router setup).
- Existing CSS:
  - `frontend/src/index.css` for global styles/tokens/layout shell.
  - `frontend/src/App.css` for template sections and component styles.

### API Client Layer

- `frontend/src/api.js` contains fetch helper functions for backend endpoints:
  - Players list/details/search
  - Games list/details
  - Player game logs / totals
  - Upcoming games
- Base URL is hardcoded to `http://127.0.0.1:5000/api`.

### Frontend Notes

- React Query is configured but not yet connected in `App.jsx` to render real API-driven homepage sections.
- Current UI is a starter layout and not yet aligned with `IDEAS.md`.

## Current Integration Contract (Frontend <-> Backend)

- Frontend is expected to call Flask endpoints under `/api`.
- Most immediate endpoint for homepage implementation:
  - `GET /api/upcoming_game` (for upcoming matches table).
- Player search can use:
  - `GET /api/search?name=...`

## Known Gaps Relevant to Homepage + Navbar Work

- No navigation component exists yet.
- No page routing exists yet.
- No dedicated homepage sections implemented yet (hero bracket, featured players, upcoming games table).
- `frontend/src/api.js` has at least one bug to address during implementation:
  - `fetchGameForPlayer` references `id` in URL string instead of the function argument `player_id`.

## Suggested Next Build Order

1. Create a shared layout shell with top navbar.
2. Build homepage sections (hero, featured players, upcoming matches).
3. Wire homepage upcoming matches to `fetchUpcomingGames` using React Query.
4. Add navbar search input wired to `fetchSearchQuery`.
5. Add placeholder pages/sections for Daily Awards, Leaders, and Teams.

