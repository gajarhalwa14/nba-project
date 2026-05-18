const BASE_URL = "http://127.0.0.1:5000/api"

export const fetchAllPlayers = async () => {
    const res = await fetch(`${BASE_URL}/player`);
    if (!res.ok) throw new Error("Failed to fetch players");
    return res.json();
}

export const fetchPlayer = async (id) => {
    const res = await fetch(`${BASE_URL}/players/${id}`);
    if (!res.ok) throw new Error("Player not found");
    return res.json();
}

export const fetchSearchQuery = async (name) => {
    const res = await fetch(`${BASE_URL}/search?name=${encodeURIComponent(name)}`);
    if (!res.ok) throw new Error("Player not found");
    return res.json();
}

export const fetchAllGames = async () => {
    const res = await fetch(`${BASE_URL}/game`);
    if (!res.ok) throw new Error("Failed to fetch games");
    return res.json(); 
}

export const fetchGame = async (id) => {
    const res = await fetch(`${BASE_URL}/games/${id}`);
    if (!res.ok) throw new Error("Game not found");
    return res.json();
}

export const fetchAllGamesForPlayer = async (id) => {
    const res = await fetch(`${BASE_URL}/players/${id}/game`);
    if (!res.ok) throw new Error("Player not found or no games to fetch");
    return res.json();
}

export const fetchGameForPlayer = async (player_id, date) => {
    const res = await fetch(`${BASE_URL}/players/${player_id}/games/${date}`);
    if (!res.ok) throw new Error("Game or player not found");
    return res.json();
}

export const fetchTotalsForPlayer = async (id) => {
    const res = await fetch(`${BASE_URL}/players/${id}/totals`);
    if (!res.ok) throw new Error("Player not found or no stats to return");
    return res.json();
}

export const fetchUpcomingGames = async () => {
    const res = await fetch(`${BASE_URL}/upcoming_game`);
    if (!res.ok) throw new Error("Games not found");
    return res.json();
}

export const fetchFeaturedPlayers = async () => {
    const res = await fetch(`${BASE_URL}/featured_players`);
    if (!res.ok) throw new Error("Featured players not found");
    return res.json();
}
