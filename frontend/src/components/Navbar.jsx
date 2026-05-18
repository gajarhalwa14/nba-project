import { useState } from 'react'

const NAV_ITEMS = [
  { key: 'home', label: 'Home' },
  { key: 'awards', label: 'Daily Awards' },
  { key: 'leaders', label: 'Leaders' },
  { key: 'teams', label: 'Teams' },
]

function Navbar({ activeView, onViewChange, onSearch, isSearching }) {
  const [searchTerm, setSearchTerm] = useState('')

  const handleSubmit = (event) => {
    event.preventDefault()
    const trimmed = searchTerm.trim()
    if (!trimmed) return
    onSearch(trimmed)
  }

  return (
    <header className="navbar">
      <div className="navbar-brand">PlayoffPicture</div>

      <nav className="navbar-links" aria-label="Primary">
        {NAV_ITEMS.map((item) => (
          <button
            key={item.key}
            type="button"
            className={`nav-link ${activeView === item.key ? 'active' : ''}`}
            onClick={() => onViewChange(item.key)}
          >
            {item.label}
          </button>
        ))}
      </nav>

      <form className="navbar-search" onSubmit={handleSubmit}>
        <input
          type="search"
          value={searchTerm}
          onChange={(event) => setSearchTerm(event.target.value)}
          placeholder="Search players"
          aria-label="Search players"
        />
        <button type="submit" disabled={isSearching}>
          {isSearching ? 'Searching...' : 'Search'}
        </button>
      </form>
    </header>
  )
}

export default Navbar
