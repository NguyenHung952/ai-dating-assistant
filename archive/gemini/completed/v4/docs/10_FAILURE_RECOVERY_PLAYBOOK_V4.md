# 10 - FAILURE RECOVERY PLAYBOOK V4

All candidate text below is synthetic and intended for pattern demonstration. It is not a guarantee of outcome.

## Global recovery rule

Do not “repair” by adding pressure.
First identify what actually failed:
- wrong topic
- wrong tone
- timing mismatch
- unsupported assumption
- unanswered question
- boundary
- natural endpoint
- ambiguous evidence

Then choose WAIT, CLOSE_NATURALLY, REPAIR, REOPEN, or a low-pressure response.

## 1. LEFT_ON_READ_RECOVERY

### Trigger
No reply after a message has been seen. Cause unknown.

### 3-day window
Không nên làm:
- “Sao seen không trả lời?”
- double-text unrelated to context
- jealousy bait

Nên làm:
- WAIT by default.
- Send only when there is a genuine new context or a previously unfinished thread worth reopening.

Candidate A:
[reopen_callback] “Hôm bữa em nói đang tìm quán yên yên, nay anh vừa đi ngang thấy một quán khá hợp gu đó.”

Candidate B:
[observation] “Nay anh mới nhớ vụ em kể hôm trước, đúng lúc thấy một chỗ khá giống.”

Candidate C:
[wait] “WAIT - không tạo tin nhắn mới chỉ để ép tiếp tục.”

Khi WAIT:
no genuine new material; uncertainty high.

Khi CLOSE_NATURALLY:
repeated low reciprocity + natural endpoint + no new context.

### 7-day window
Không nên làm:
- demand explanation
- mention read receipt
- “chắc em bận lắm”

Nên làm:
- one new, context-relevant opener at most.
- keep intensity below prior level unless new evidence supports otherwise.

Candidate A:
[reopen_callback] “Tình cờ lại thấy món em từng nhắc, giờ mới hiểu sao em mê nó.”

Candidate B:
[self-share + open loop] “Anh vừa thử món đó rồi, có một điểm đúng như em tả nhưng cũng khác kha khá.”

Candidate C:
[wait] “Nếu không có material mới: WAIT.”

### 14-day window
Không nên làm:
- escalating message sequence
- guilt
- emotional accounting

Nên làm:
- treat as a new episode.
- one low-pressure attempt only if there is a genuine reason.
- otherwise CLOSE_NATURALLY and move on.

Candidate A:
[observation] “Lâu rồi mới nhớ tới vụ quán hôm trước, chỗ đó cuối cùng anh cũng thử rồi.”

Candidate B:
[new_episode] “Tự nhiên hôm nay nhớ vụ em kể về ___, thấy cũng buồn cười.”

Candidate C:
[close_naturally] “CLOSE_NATURALLY - không tiếp tục nếu không có lý do thực.”

## 2. CONVERSATION_DIED_RECOVERY

### Trigger
Several turns contain little expansion and no new reciprocal material.

Không nên làm:
- question stacking
- “sao em lạnh vậy?”

Nên làm:
- shift once to a real adjacent topic, then stop if it does not revive.

Candidate A:
[callback] “Vụ hôm trước em kể vẫn còn buồn cười thật, nhất là đoạn đó.”

Candidate B:
[self-share + open loop] “Anh vừa gặp đúng kiểu tình huống em từng kể, lúc đó mới thấy em nói chuẩn.”

Candidate C:
[wait] “Nếu vẫn cụt sau một lần bridge: WAIT.”

## 3. WRONG_MESSAGE_RECOVERY

### Trigger
User sent wording that was too long, too flirty, off-topic, or presumptive.

Không nên làm:
- 3 follow-up apologies
- explain the whole AI strategy
- pretend nothing happened if the mismatch is obvious

Nên làm:
- one clean repair when repair is warranted.

Candidate A:
[repair] “Nãy anh nói hơi quá tay, ý anh chỉ đang đùa nhẹ thôi.”

Candidate B:
[repair + close] “Câu nãy hơi dài thật, bỏ qua đoạn đó nha.”

Candidate C:
[wait] “Nếu người kia đã tiếp tục bình thường: không cần repair lần hai.”

## 4. REJECTION_GRACEFUL_EXIT

### Trigger
Clear no, clear disinterest, explicit boundary, or refusal.

Không nên làm:
- persuade
- ask why repeatedly
- last-chance offer

Nên làm:
- accept with dignity.

Candidate A:
[close_naturally] “Ừ anh hiểu, cảm ơn em nói thẳng nha.”

Candidate B:
[close_naturally] “Ok, anh tôn trọng vậy nha, chúc em mọi thứ thuận lợi.”

Candidate C:
[wait] “WAIT - không gửi thêm để đổi quyết định của người kia.”

## 5. MIXED_SIGNAL_HANDLING

### Trigger
Signals point in different directions across several turns.

Không nên làm:
- choose the most flattering interpretation
- infer hidden attraction
- run “tests”

Nên làm:
- lower certainty and pressure.
- judge repeated pattern over isolated moments.

Candidate A:
[observation] “Có lúc mình nói chuyện khá vào gu, có lúc lại cụt nên anh để tự nhiên thôi.”

Candidate B:
[self-share] “Anh cứ nói chuyện theo nhịp hiện tại, không cần ép nó thành gì cả.”

Candidate C:
[wait] “Nếu evidence vẫn mixed và không có live topic: WAIT.”

## 6. BOUNDARY_PUSHED_RECOVERY

### Trigger
User noticed that they pushed too hard or the other person stated discomfort.

Không nên làm:
- explain intent as excuse
- “anh chỉ thử thôi”
- push once more

Nên làm:
- acknowledge, own the impact, stop.

Candidate A:
[repair] “Ừ, đoạn đó anh đi hơi quá, anh dừng ở đây nha.”

Candidate B:
[repair + boundary] “Anh hiểu ý em rồi, anh tôn trọng ranh giới đó.”

Candidate C:
[close_naturally] “Mình để chuyện đó sang một bên nha.”

## 7. JEALOUSY_TRAP_HANDLING

### Trigger
A third person is mentioned and user wants to create rivalry.

Không nên làm:
- insult the rival
- compete for status
- “em chọn ai?”
- punish/withdraw strategically

Nên làm:
- answer the actual context without entering competition.

Candidate A:
[observation] “Nghe như em đang kể một câu chuyện thôi, anh không cần biến nó thành cuộc thi đâu.”

Candidate B:
[self-share] “Anh thích nói chuyện trực tiếp hơn là đo mình với ai khác.”

Candidate C:
[wait] “Nếu chủ đề đang cố kéo sang rivalry: WAIT hoặc CLOSE_NATURALLY.”

## Recovery ladder

MATCH -> ACKNOWLEDGE -> REPAIR -> WAIT -> REOPEN_ON_REAL_CONTEXT -> CLOSE_NATURALLY

Never:
ESCALATE -> PRESSURE -> MANIPULATE -> TEST
