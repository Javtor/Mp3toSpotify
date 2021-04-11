import musicbrainzngs

musicbrainzngs.auth("user", "password")
musicbrainzngs.set_useragent("Example music app", "0.1", "http://example.com/music")


artist_id = "2e22535a-4d53-43df-98d7-7220cf91ef79"
try:
    result = musicbrainzngs.get_recording_by_id(artist_id)
except WebServiceError as exc:
    print("Something went wrong with the request: %s" % exc)
else:
    # artist = result["artist"]
    # print("name:\t\t%s" % artist["name"])
    # print("sort name:\t%s" % artist["sort-name"])
    print(result)