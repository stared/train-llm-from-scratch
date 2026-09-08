# Chłopaki nie płaczą: screenplay search

Searched September 7, 2026, for a full screenplay of the **2000 film**, written by **Mikołaj Korzyński**. **No verified publicly downloadable full screenplay was found.** This is a search result, not proof that a copy does not exist. No screenplay or subtitles have been added to the training data.

**Later update:** the user supplied `datasets/chlopaki.md`. That local dialogue text is now used for [a separate bidirectional fine-tuning experiment](CHLOPAKI.md). Its provenance is explicitly the supplied file; it has not been independently verified as the official screenplay. The search findings below remain historical.

## Useful sources and what they actually contain

| Source | What was found | Use |
|---|---|---|
| [Studio Filmowe Zebra: film page](https://www.zebrafilm.pl/filmy/169-chlopaki-nie-placza) | Official film information and writer credit; indexed page available, direct fetch returned an error | Production/source lead; no script download verified |
| [FilmPolski: film record](https://www.filmpolski.pl/fp/index.php/127827) | Credits, synopsis, writer Mikołaj Korzyński | Verify the film and authorship, not screenplay text |
| [Script Fiesta 2025 programme](https://liceumfilmowe.pl/pl/lf/C_WSFO.LF/1660/program-13.-script-fiesty%21) | Panel on the screenplay's 25th anniversary, with Olaf Lubaszenko and Mikołaj Korzyński | Specific lead for locating the original script; not a published script |
| [Panel recording](https://www.youtube.com/watch?v=voxZf3yvbSk) | Recording listed for that Script Fiesta panel | Discussion of writing, not the film transcript |
| [Mrągowo library catalogue](https://www.mragowo-ckit.sowa.pl/index.php?001=MRA+P20001243&KatID=0&typ=record) | DVD edition, despite matching “scenariusz” in the catalogue credit | Not a screenplay manuscript or text edition |
| [Wikicytaty](https://pl.wikiquote.org/wiki/Ch%C5%82opaki_nie_p%C5%82acz%C4%85) | Selected dialogue quotations | Incomplete quote collection; not an ordered full screenplay |
| [Polish film teaching material](https://www.sjikp.us.edu.pl/wp-content/uploads/agatambor.pdf) | Film description, credits and educational material | Search false positive for a downloadable screenplay |
| [Writer's account of the film](https://kultura.onet.pl/film/wiadomosci/scenarzysta-mikolaj-korzynski-o-pracy-nad-filmem-chlopaki-nie-placza/kjhx5c4) | Discussion by the screenwriter of his material and characters | Background on the writing, not full dialogue |

Queries included Polish title with accents and ASCII spelling, “scenariusz”, “tekst”, “PDF”, “download”, “screenplay”, “transcript”, library records, and Polish subtitles. Results also mixed in a song, a 2005 game, other similarly titled films and school-event scripts.

## Practical next route

The strongest leads are the credited writer/production organisation and the Script Fiesta organisers, who hosted a panel specifically about this screenplay. No one has been contacted. A script supplied by the author or a verified published edition would let us build an actual dialogue dataset with provenance.

Subtitles would be a different source: timed fragments usually lack scene descriptions and reliable speaker labels. They should be labelled as subtitles, not silently presented as a screenplay. The current [comic dataset](datasets/wit-v1/train.jsonl) remains original assistant-authored material, clearly separate from this search.
