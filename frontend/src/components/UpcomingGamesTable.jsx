import { useQuery } from '@tanstack/react-query'
import { fetchUpcomingGames } from '../api'

function UpcomingGamesTable() {
  const {
    data: games = [],
    isLoading,
    isError,
    error,
  } = useQuery({
    queryKey: ['upcomingGames'],
    queryFn: fetchUpcomingGames,
  })

  return (
    <section className="view-card">
      <h2>Upcoming Matches</h2>

      {isLoading ? <p>Loading upcoming games...</p> : null}

      {isError ? <p>{error.message || 'Failed to load upcoming games.'}</p> : null}

      {!isLoading && !isError && games.length === 0 ? (
        <p>No upcoming games available.</p>
      ) : null}

      {!isLoading && !isError && games.length > 0 ? (
        <div className="table-wrap">
          <table className="upcoming-games-table">
            <thead>
              <tr>
                <th>Game</th>
                <th>Status</th>
                <th>Time (ET)</th>
                <th>Conference</th>
                <th>Round</th>
              </tr>
            </thead>
            <tbody>
              {games.map((game) => (
                <tr key={game.gameid}>
                  <td>{game.gamelabel || game.gamesublabel || 'N/A'}</td>
                  <td>{game.gamestatustext || 'N/A'}</td>
                  <td>{game.gameet || 'N/A'}</td>
                  <td>{game.seriesconference || 'N/A'}</td>
                  <td>{game.porounddesc || game.seriesgamenumber || 'N/A'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ) : null}
    </section>
  )
}

export default UpcomingGamesTable
