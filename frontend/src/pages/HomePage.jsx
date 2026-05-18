import HeroBracket from '../components/HeroBracket'
import FeaturedPlayers from '../components/FeaturedPlayers'
import UpcomingGamesTable from '../components/UpcomingGamesTable'

function HomePage() {
  return (
    <div className="home-page">
      <HeroBracket />
      <FeaturedPlayers />
      <UpcomingGamesTable />
    </div>
  )
}

export default HomePage
