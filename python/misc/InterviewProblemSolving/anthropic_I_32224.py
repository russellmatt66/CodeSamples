# Code file for the technical interview with Anthropic
def convert_to_trace(samples: list[Sample]) -> list[Event]:
    event_list = []
    prev_stack = []

    for sample in samples:
        for stack_element in samples.stack:
            if not prev_stack:
                prev_stack = samples.stack
                for element in prev_stack:
                    event_list.append(Event('start',sample.ts,element))
            i = 0
            if (stack_element == prev_stack[i]):
                i += 1
            else:
                for j in range(i,len(samples.stack)):
                    event_list.append(Event('end',sample.ts,prev_stack[j]))

    return event_list