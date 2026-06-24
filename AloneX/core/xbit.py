# ALONE-CODER
import aiohttp

class XBitAPI:
    def __init__(self):
        from AloneX import config
        self.xbit_api_key = config.XBIT_API_TOKEN
        self.xbit_base_url = config.XBIT_API_URL
        self.aru_api_key = config.ARU_API_KEY
        self.aru_base_url = config.ARU_API_URL

    async def get_info(self, vid_id: str):
        # Try ARU first
        if self.aru_api_key and self.aru_base_url:
            endpoint = f"{self.aru_base_url}/info/{vid_id}"
            params = {'api_key': self.aru_api_key}
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(endpoint, params=params) as response:
                        if response.status == 200:
                            data = await response.json()
                            if data.get('status') == 'success':
                                return data
            except Exception as e:
                print(f"Error fetching from ARU API: {e}")
        
        # Fallback to XBit
        if self.xbit_api_key and self.xbit_base_url:
            endpoint = f"{self.xbit_base_url}/info/{vid_id}"
            headers = {
                'x-api-key': self.xbit_api_key,
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
        # Try ARU first
        if self.aru_api_key and self.aru_base_url:
            endpoint = f"{self.aru_base_url}/search"
            params = {'query': query, 'api_key': self.aru_api_key}
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(endpoint, params=params) as response:
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
                print(f"Error searching from ARU API: {e}")
        
        # Fallback to XBit
        if self.xbit_api_key and self.xbit_base_url:
            endpoint = f"{self.xbit_base_url}/search"
            params = {'query': query}
            headers = {'x-api-key': self.xbit_api_key}
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
        # Try ARU first
        if self.aru_api_key and self.aru_base_url:
            endpoint = f"{self.aru_base_url}/playlist"
            params = {'url': url, 'limit': limit, 'api_key': self.aru_api_key}
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(endpoint, params=params) as response:
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
                print(f"Error fetching playlist from ARU API: {e}")
        
        # Fallback to XBit
        if self.xbit_api_key and self.xbit_base_url:
            endpoint = f"{self.xbit_base_url}/playlist"
            params = {'url': url, 'limit': limit}
            headers = {'x-api-key': self.xbit_api_key}
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

        youtube_url = f"https://www.youtube.com/watch?v={vid_id}"
        
        # Try ARU first
        if self.aru_api_key and self.aru_base_url:
            endpoint = f"{self.aru_base_url}/download"
            params = {
                'url': youtube_url,
                'type': 'video' if video else 'audio',
                'api_key': self.aru_api_key
            }
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(endpoint, params=params, timeout=60) as response:
                        if response.status == 200:
                            with open(path, "wb") as f:
                                async for chunk in response.content.iter_chunked(1024 * 1024):
                                    f.write(chunk)
                            if os.path.exists(path) and os.path.getsize(path) > 1024:
                                print(f"Successfully downloaded {vid_id} using ARU API")
                                return path
                            else:
                                print(f"Downloaded file is too small or missing for {vid_id} (ARU)")
                        else:
                            print(f"ARU API download failed with status {response.status} for {vid_id}")
            except Exception as e:
                print(f"Error downloading from ARU API: {e}")
        
        # Try XBit
        if self.xbit_api_key and self.xbit_base_url:
            endpoint = f"{self.xbit_base_url}/download"
            params = {
                'url': youtube_url,
                'type': 'video' if video else 'audio',
                'api_key': self.xbit_api_key
            }
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(endpoint, params=params, timeout=60) as response:
                        if response.status == 200:
                            with open(path, "wb") as f:
                                async for chunk in response.content.iter_chunked(1024 * 1024):
                                    f.write(chunk)
                            if os.path.exists(path) and os.path.getsize(path) > 1024:
                                print(f"Successfully downloaded {vid_id} using XBit API")
                                return path
                            else:
                                print(f"Downloaded file is too small or missing for {vid_id} (XBit)")
                        else:
                            print(f"XBit API download failed with status {response.status} for {vid_id}")
            except Exception as e:
                print(f"Error downloading from XBit API: {e}")
        
        # Fallback to yt-dlp
        print(f"Falling back to YouTube download for {vid_id}...")
        from AloneX import yt
        return await yt.download(vid_id, video=video)