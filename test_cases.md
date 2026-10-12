
| Test | Input / Action | Expected result |
|---|---|---|
| 1. Normal reading | Enter `24` | Classification is `NORMAL` |
| 2. Lower boundary | Enter `29` | Classification is `NORMAL` |
| 3. Warning lower boundary | Enter `30` | Classification is `WARNING` |
| 4. Warning upper boundary | Enter `35` | Classification is `WARNING` |
| 5. Critical reading | Enter `36` | Classification is `CRITICAL` |
| 6. Maximum accepted reading | Enter `100` | Accepted and classified as `CRITICAL` |
| 7. Negative reading | Enter `-1` | Rejected; asks again |
| 8. Text input | Enter `hot` | Rejected; asks again |
| 9. Decimal input | Enter `31.5` | Rejected because this version requires whole numbers |
| 10. Invalid menu | Select `9` | Error message; menu repeats |
| 11. Critical alert | Readings `28, 31, 37` | Diagnostic scan identifies the critical device and displays red alert |
| 12. Warning-only alert | Readings `28, 30, 29` | Yellow notice |
| 13. All-normal status | Readings `20, 25, 29` | Green status |
| 14. Add reading | Choose option 2 and enter `40` | Reading is appended and appears in later reports |
| 15. Exit | Choose option 5 | Program displays shutdown message and ends 