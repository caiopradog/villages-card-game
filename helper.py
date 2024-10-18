from copy import deepcopy


def print_options(options, chosen, page_count, end=False, hide_options=True):
    print_text = ''
    if not hide_options and len(options) > 0:
        option_pad = max([len(str(opt)) for opt in options]) + len(str(len(options)))
        num_pad = len(str(len(options)))

        shown_options = 0
        for (idx, option) in enumerate(options):
            if option not in chosen:
                if shown_options % page_count == 0 and shown_options != 0:
                    print_text += '\n'
                elif len(print_text) > 0:
                    print_text += ' | '
                text = option.title().ljust(option_pad, ' ')
                print_text += f'{str(idx+1).rjust(num_pad, '0')}: {text}'
                shown_options += 1
    print_text += '\nClear: Clear selection'
    if end:
        print_text += ' | End or Empty: End selection'
    print(print_text)


def choose_option(
    original_options,
    text='Choose an option: ',
    optional=True,
    page_count=5,
    min_choice: int = 1,
    max_choice: int = 1
):
    max_choice = len(original_options) if max_choice < 0 else max_choice

    remaining_options = list(original_options)
    end_selection = False
    chosen = []
    while not end_selection:
        can_end_selection = len(chosen) >= min_choice
        all_selected = len(chosen) == max_choice
        if all_selected:
            end_selection = True
            continue
        print(text, f'Min: {min_choice} | Max: {max_choice} | Selected: {chosen} | {'Optional' if optional else ''}')
        print_options(original_options, chosen, page_count, can_end_selection or optional, all_selected)
        try:
            option = input(text)
            if option.lower() == 'end' or option.lower() == '':
                if len(chosen) == 0 and optional or (len(chosen) >= min_choice):
                    end_selection = True
                else:
                    print('Min qtd not selected!')
                continue
            if option.lower() == 'clear':
                remaining_options = list(original_options)
                chosen = []
                continue
            option = int(option)
            chosen_option = original_options[option - 1]
            if all_selected or option > len(original_options) or (option == 0 and not optional) or chosen_option in chosen:
                raise ValueError
            remaining_options.remove(chosen_option)
            chosen.append(chosen_option)
        except ValueError:
            print('Invalid option!')
    return None if len(chosen) == 0 else chosen[0] if len(chosen) == 1 else chosen
