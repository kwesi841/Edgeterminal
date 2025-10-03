import { useQuery } from '@tanstack/react-query'
import axios from 'axios'

export default function Tokens() {
  const { data } = useQuery({
    queryKey: ['tokens'],
    queryFn: async () => (await axios.get('/api/tokens?limit=25')).data,
  })

  return (
    <div style={{ color: '#eaeaea', background: '#0c0c0f', minHeight: '100vh', padding: 24 }}>
      <h1>Tokens</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  )
}
