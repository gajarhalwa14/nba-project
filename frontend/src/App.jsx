import { useState } from 'react'
import Navbar from './components/Navbar'
import HomePage from './pages/HomePage'
import { fetchSearchQuery } from './api'
import './App.css'

function App() {
  const [activeView, setActiveView] = useState('home')
  const [searchState, setSearchState] = useState({
    status: 'idle',
    query: '',
    result: null,
    error: '',
  })

  const handleSearch = async (searchTerm) => {
    const trimmed = searchTerm.trim()
    if (!trimmed) {
      setSearchState({
        status: 'error',
        query: '',
        result: null,
        error: 'Please enter a player name.',
      })
      return
    }

    setSearchState({
      status: 'loading',
      query: trimmed,
      result: null,
      error: '',
    })

    try {
      const player = await fetchSearchQuery(trimmed)
      setSearchState({
        status: 'success',
        query: trimmed,
        result: player,
        error: '',
      })
    } catch (error) {
      setSearchState({
        status: 'error',
        query: trimmed,
        result: null,
        error: error.message || 'Search failed.',
      })
    }
  }

  const renderView = () => {
    if (activeView === 'home') {
      return <HomePage />
    }

    if (activeView === 'awards') {
      return (
        <section className="view-card">
          <h1>Daily Awards</h1>
          <p>Placeholder view for the upcoming awards section.</p>
        </section>
      )
    }

    if (activeView === 'leaders') {
      return (
        <section className="view-card">
          <h1>Leaders</h1>
          <p>Placeholder view for leaderboard tables and filters.</p>
        </section>
      )
    }

    return (
      <section className="view-card">
        <h1>Teams</h1>
        <p>Placeholder view for playoff teams and team profiles.</p>
      </section>
    )
  }

  return (
    <div className="app-shell">
      <Navbar
        activeView={activeView}
        onViewChange={setActiveView}
        onSearch={handleSearch}
        isSearching={searchState.status === 'loading'}
      />

      <main className="page-content">
        {searchState.status === 'error' ? (
          <section className="search-feedback">
            <strong>Search error:</strong> {searchState.error}
          </section>
        ) : null}

        {searchState.status === 'success' && searchState.result ? (
          <section className="search-feedback">
            <h2>Search Result</h2>
            <p>
              <strong>Name:</strong> {searchState.result.player}
            </p>
            <p>
              <strong>Team ID:</strong> {searchState.result.team_id ?? 'N/A'}
            </p>
            <p>
              <strong>Position:</strong> {searchState.result.pos || 'N/A'}
            </p>
            <p>
              <strong>Player ID:</strong> {searchState.result.player_id ?? 'N/A'}
            </p>
          </section>
        ) : null}

        {renderView()}
      </main>
    </div>
  )
}

export default App
