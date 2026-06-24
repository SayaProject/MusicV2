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
        return None

    async def search(self, query: str, message_id: int, video: bool = False):
        return None

    async def playlist(self, limit: int, mention: str, url: str, video: bool = False):
        return None

    async def download(self, vid_id: str, video: bool = False):
        import os
        path = f"downloads/{vid_id}.{'mp4' if video else 'mp3'}"
        if os.path.exists(path):
            return path

        youtube_url = f"https://www.youtube.com/watch?v={vid_id}"
        
        # Try ARU first with direct URL for fast play
        if self.aru_api_key and self.aru_base_url:
            direct_url = f"{self.aru_base_url}/download?url={youtube_url}&type={'video' if video else 'audio'}&api_key={self.aru_api_key}"
            # Verify the URL is reachable first
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.head(direct_url, timeout=10) as resp:
                        if resp.status == 200:
                            print(f"Successfully got direct URL for {vid_id} using ARU API")
                            return direct_url
            except Exception as e:
                print(f"Error checking ARU direct URL for {vid_id}: {e}")
            
            # If direct URL didn't work, download the file
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(direct_url, timeout=300) as response:
                        if response.status == 200:
                            with open(path, "wb") as f:
                                async for chunk in response.content.iter_chunked(1024 * 1024):  # 1MB chunks for speed
                                    f.write(chunk)
                            if os.path.exists(path) and os.path.getsize(path) > 1024:
                                print(f"Successfully downloaded {vid_id} using ARU API")
                                return path
                            else:
                                print(f"Downloaded file is too small or missing for {vid_id} (ARU)")
            except Exception as e:
                print(f"Error downloading from ARU API: {e}")
        
        # Fallback to yt-dlp
        print(f"Falling back to YouTube download for {vid_id}...")
        from AloneX import yt
        return await yt.download(vid_id, video=video)
