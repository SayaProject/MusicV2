# ALONE-CODER
import aiohttp

class XBitAPI:
    def __init__(self):
        from AloneX import config
        self.api_key = config.XBIT_API_TOKEN
        self.base_url = config.XBIT_API_URL

    async def get_info(self, vid_id: str):
        if not self.api_key:
            return None
        
        endpoint = f"{self.base_url}/info/{vid_id}"
        headers = {
            'x-api-key': self.api_key,
            'Content-Type': 'application/json'
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint, headers=headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        if data.get('status') == 'success':
                            return data
        except Exception as e:
            print(f"Error fetching from XBit API: {e}")
        
        return None

    async def search(self, query: str, message_id: int, video: bool = False):
        if not self.api_key:
            return None
        
        endpoint = f"{self.base_url}/search"
        params = {'query': query}
        headers = {'x-api-key': self.api_key}
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint, params=params, headers=headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        if data.get('status') == 'success' and data.get('results'):
                            from AloneX.helpers._dataclass import Media
                            res = data['results'][0]
                            return Media(
                                id=res['id'],
                                title=res['title'],
                                duration=res['duration'],
                                duration_sec=res['duration_sec'],
                                url=res['url'],
                                file_path=None,
                                message_id=message_id,
                                video=video
                            )
        except Exception as e:
            print(f"Error searching from XBit API: {e}")
        return None

    async def playlist(self, limit: int, mention: str, url: str, video: bool = False):
        if not self.api_key:
            return None
        
        endpoint = f"{self.base_url}/playlist"
        params = {'url': url, 'limit': limit}
        headers = {'x-api-key': self.api_key}
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint, params=params, headers=headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        if data.get('status') == 'success' and data.get('results'):
                            from AloneX.helpers._dataclass import Track
                            tracks = []
                            for res in data['results']:
                                tracks.append(Track(
                                    id=res['id'],
                                    channel_name=res.get('channel', "Unknown"),
                                    duration=res['duration'],
                                    duration_sec=res['duration_sec'],
                                    title=res['title'],
                                    url=res['url'],
                                    user=mention,
                                    video=video
                                ))
                            return tracks
        except Exception as e:
            print(f"Error fetching playlist from XBit API: {e}")
        return None

    async def download(self, vid_id: str, video: bool = False):
        path = f"downloads/{vid_id}.{'mp4' if video else 'mp3'}"
        import os
        if os.path.exists(path):
            return path

        if self.api_key:
            # Use the new API endpoint format
            youtube_url = f"https://www.youtube.com/watch?v={vid_id}"
            endpoint = f"{self.base_url}/download"
            params = {
                'url': youtube_url,
                'type': 'video' if video else 'audio',
                'api_key': self.api_key
            }
            
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(endpoint, params=params, timeout=60) as response:
                        if response.status == 200:
                            with open(path, "wb") as f:
                                async for chunk in response.content.iter_chunked(1024 * 1024):
                                    f.write(chunk)
                            if os.path.exists(path) and os.path.getsize(path) > 1024:
                                print(f"Successfully downloaded {vid_id} using new API")
                                return path
                            else:
                                print(f"Downloaded file is too small or missing for {vid_id}")
                        else:
                            print(f"API download failed with status {response.status} for {vid_id}")
                            error_text = await response.text()
                            print(f"Error response: {error_text}")
            except Exception as e:
                print(f"Error downloading from new API: {e}")
        
        print(f"Falling back to YouTube download for {vid_id}...")
        from AloneX import yt
        return await yt.download(vid_id, video=video)
