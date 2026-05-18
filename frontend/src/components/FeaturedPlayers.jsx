import { useQuery } from '@tanstack/react-query'
import { fetchFeaturedPlayers } from '../api'

function FeaturedPlayers() {
  const {
    data: players = [],
    isLoading,
    isError,
    error,
  } = useQuery({
    queryKey: ['featuredPlayers'],
    queryFn: fetchFeaturedPlayers,
  })

  return (
    <section className="view-card">
      <h2>Featured Players</h2>

      {isLoading ? <p>Loading featured players...</p> : null}

      {isError ? <p>{error.message || 'Failed to load featured players.'}</p> : null}

      {!isLoading && !isError && players.length === 0 ? (
        <p>No featured players available.</p>
      ) : null}

      {!isLoading && !isError && players.length > 0 ? (
        <ul className="featured-player-list">
          {players.map((player) => (
            <li key={player.personid} className="featured-player-item">
              <h3>{player.name}</h3>
              <p>
                {player.position || 'N/A'} #{player.jerseynum || 'N/A'}
              </p>
              <p>
                PTS: {player.points ?? 'N/A'} | REB: {player.rebounds ?? 'N/A'} | AST:{' '}
                {player.assists ?? 'N/A'}
              </p>
            </li>
          ))}
        </ul>
      ) : null}
    </section>
  )
}

export default FeaturedPlayers
